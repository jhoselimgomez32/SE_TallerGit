import argparse


def say_hello(name="World"):
    print("Hello ", name, "!")


parse = argparse.ArgumentParser(description='say hello.')
parse.add_argument('--name', type=str, required=False,
                   metavar='name', help='your name', default='World')
args = parse.parse_args()
say_hello(args.name)
