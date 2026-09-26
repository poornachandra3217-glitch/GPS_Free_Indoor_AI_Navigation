import os
import cv2

class VisualLocalizer:
    def __init__(self, folder):
        self.folder = folder
        self.orb = cv2.ORB_create(nfeatures=1500, scaleFactor=1.2, nlevels=8)
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
        self.references = {}
        self._load_references()

    def _load_references(self):
        os.makedirs(self.folder, exist_ok=True)
        for name in os.listdir(self.folder):
            path = os.path.join(self.folder, name)
            if not name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                continue
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue
            keypoints, descriptors = self.orb.detectAndCompute(image, None)
            if descriptors is not None and len(keypoints) >= 8:
                node = os.path.splitext(name)[0]
                self.references[node] = {"keypoints": keypoints, "descriptors": descriptors}

    def localize(self, image):
        if not self.references:
            return {
                "localized": False,
                "message": "No reference images found. Add photos to reference_images/.",
                "best_node": None, "confidence": 0
            }

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = self.orb.detectAndCompute(gray, None)
        if descriptors is None or len(keypoints) < 8:
            return {
                "localized": False,
                "message": "Not enough visual features detected.",
                "best_node": None, "confidence": 0
            }

        scores = []
        for node, ref in self.references.items():
            matches = self.matcher.knnMatch(descriptors, ref["descriptors"], k=2)
            good = []
            for pair in matches:
                if len(pair) == 2:
                    m, n = pair
                    if m.distance < 0.72 * n.distance:
                        good.append(m)
            ratio = len(good) / max(1, min(len(descriptors), len(ref["descriptors"])))
            scores.append((ratio, len(good), node))

        scores.sort(reverse=True)
        best_ratio, good_matches, best_node = scores[0]
        confidence = round(min(100.0, best_ratio * 1000), 1)
        localized = good_matches >= 12 and confidence >= 8

        return {
            "localized": localized,
            "best_node": best_node if localized else None,
            "confidence": confidence,
            "good_matches": good_matches,
            "message": f"Likely location: {best_node}" if localized
                       else "Localization confidence is too low. Try another view."
        }
