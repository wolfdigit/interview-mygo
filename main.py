"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can
 
After you finish coding, please push to your GitHub account and share the link with us.
"""
 
# Please write a function to reverse the following nested input value into output value
 
# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}
 
# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

def main():
    from Solve import Solve

    #output = Solve.solve(input_value)
    #print(output)

    from Test import Test
    Test.runAll(Solve.solve)

if __name__ == '__main__':
    main()