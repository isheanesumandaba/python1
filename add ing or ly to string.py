#code to add ly or ing to a string


def verbing(s):
        if len(s) < 3:
                    return s
         elif s.endswith('ing'):
                    return s + 'ly'
         else:
                     return s + 'ing'


