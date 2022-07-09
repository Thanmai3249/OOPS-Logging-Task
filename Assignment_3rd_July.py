import logging

logging.basicConfig(filename='Tasks.log', level = logging.INFO)

class task:
    '''
    1. Try to print a prime number in between 1 to 1000
    '''
    def primenumber(self, n):
        try:
            logging.info('Printing prime numbers between 1 to 1000')
            for number in range(1,n):
                if number>1:
                    for i in range(2, number):
                        if (number%i) == 0:
                            break
                    else:
                        print(number)
        except Exception as e:
            logging.exception('Check the logic once')
    '''
    2. Try to extract all the numerical data it may b a part of dict key and values
    '''
    def extractingnumdata(self, l):
        try:
            logging.info('Extracting all the numerical data from the given list')
            l1 = []
            for i in l:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == set:
                    for s in i:
                        if type(s) == int:
                            l1.append(s)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l1.append(k)
                            l1.append(v)
                            print(l1)
        except Exception as e:
            logging.exception('Check the logic once')


obj = task()
print(obj.primenumber(1000))
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
print(obj.extractingnumdata(l))
