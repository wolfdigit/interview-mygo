class Test:
    input_value = [
        {
          'hired': {
            'be': {
              'to': {
                'deserve': 'I'
              }
            }
          }
        },
        {'a':'b'},
        {'a':{'b':'c'}},
        {},
        'a',
        {'a':{'b':{}}},
        {'a':{'b':''}, 'a2':'b2'}
    ]
    output_value = [
        {
          'I': {
            'deserve': {
              'to': {
                 'be': 'hired'
              }
            }
          }
        },
        {'b':'a'},
        {'c':{'b':'a'}},
        {},
        'a',
        {'b':'a'},
        {'':{'b':'a'}}
    ]

    def __init__(self, cb, caseId):
        self.callback = cb
        self.input_v = self.input_value[caseId]
        self.answer = self.output_value[caseId]
        
    def run(self):
        print("===input:===")
        print(self.input_v)
        output = self.callback(self.input_v)
        print("===expect:===")
        print(self.answer)
        print("===output:===")
        print(output)
    
    @classmethod
    def runAll(cls, cb):
        for i in range(0, len(cls.input_value)):
            inst = Test(cb, i)
            inst.run()
            print("")