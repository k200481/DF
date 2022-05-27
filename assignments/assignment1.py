import argparse
import rsa

def dump(device_name, block_size):
    ifil = open(device_name, 'rb')
    ofil = open(f'{device_name}_img', 'wb')
    bytes = 'temp'
    while bytes:
        bytes = ifil.read(block_size)
        ofil.write(bytes)

def sign(device_name, sk):
    fil = open(device_name, 'rb')
    return rsa.sign(fil, sk, 'SHA-1')

def verify(device_name, pk, sgn):
    f = open(device_name, 'rb')
    rsa.verify(f, sgn, pk)
    print('verified')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('device_name')
    parser.add_argument('block_size')
    parser.add_argument('option')
    parser.add_argument('-k')
    parser.add_argument('-s')
    args = parser.parse_args()

    device_name = args.device_name
    block_size = args.block_size

    if args.option == 'd':
        dump(device_name, int(block_size))
        if not args.k:
            pk, sk = rsa.newkeys(512)
            open('pk.pem', 'wb').write(pk.save_pkcs1())
            open('sk.pem', 'wb').write(sk.save_pkcs1())
            print('new pk and sk generated')
            sgn = sign(device_name, rsa.PrivateKey.load_pkcs1(open('sk.pem', 'rb').read()))
        else:
            sgn = sign(device_name, rsa.PrivateKey.load_pkcs1(open(args.k, 'rb').read()))
        open('signature', 'wb').write(sgn)
    elif args.option == 'v':
        if args.k and args.s:
            verify(device_name, rsa.PublicKey.load_pkcs1(open(args.k, 'rb').read()), open(args.s, 'rb').read())
        else:
            print('need a public key and signature to verify')
