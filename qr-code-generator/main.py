import qrcode
import argparse

def generate_qr(url):
    img = qrcode.make(url)
    img.save("qr_codes/my_qr.png")
    print(f"QR code generated for: {url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://github.com/kaw393939", help="URL to encode in QR")
    args = parser.parse_args()

    generate_qr(args.url)
