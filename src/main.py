import argparse

import cv2

def parse_args():
    parser = argparse.ArgumentParser(description="Indoor location system")

    subparsers = parser.add_subparsers(dest="aruco")
    aruco_parser = subparsers.add_parser("aruco", help="Generate ArUco marker")
    aruco_parser.add_argument(
        "--gen",
        action="store_true",
        help="Generate ArUco marker",
    )
    return parser.parse_args()

def generate_aruco_marker(marker_id, marker_size):
    # Generate an ArUco marker with the specified ID and size
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
    return marker_image

def main():
    args = parse_args()
    if args.gen:
        for marker_id in range(0, 250):
            marker_size = 200
            marker_image = generate_aruco_marker(marker_id, marker_size)
            cv2.imwrite(f"../markers/marker_{marker_id}.png", marker_image)
            print(f"Generated ArUco marker with ID {marker_id} and saved as marker_{marker_id}.png")
    else:
        pass

    print("Indoor location system")

if __name__ == "__main__":
    main()
