import argparse

from mjcf2urdf import convert_mjcf_to_urdf


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_mjcf', type=str,
                        help='MuJoCo xml file to be converted to URDF')
    parser.add_argument('--out', '-o', help='Output Directory Name',
                        default='result')
    args = parser.parse_args()

    convert_mjcf_to_urdf(args.input_mjcf, args.out)


if __name__ == '__main__':
    main()
