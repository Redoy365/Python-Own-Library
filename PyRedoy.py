
class Machine:

    def __init__(self) -> None:
        pass
    
#   std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()  std()       
    def std(speed):
        count = 0

        for i in range(len(speed)):

            count = count + speed[i]

        x = count/len(speed)

        j = 0
        for i in range(len(speed)):

            y = speed[i] - x

            z = y**2

            j = j + z

        x1 = j/len(speed)

        return (x1**(1/2))
    
#   mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()  mean()
    def mean(para):
        count = 0
        for i in range(len(para)):
            count = count + para[i]

        x = count/len(para)
        return x






