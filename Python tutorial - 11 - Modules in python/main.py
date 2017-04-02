#import some functions only
from calculation import add2Numbers, minus2Numbers, multiply2Numbers
import pprint

if __name__=='__main__':
    pprint.pprint(add2Numbers(10, 20))
    pprint.pprint(minus2Numbers(10, 20))
    pprint.pprint(multiply2Numbers(10, 20))