from IPython import embed
#embed()

class PythonDevEnv:    

    def __init__(self):        
        pass

    def histogramArea(self,arr):
        print(arr)
        numBars = len(arr)
        #print(numBars)

        maxArea=0
        # for all combinations
        for i in range(numBars):
            for j in range(i, numBars):
                # for all combinations of rectangles 
                #  determine the minHeight

                #print(i,j)                
                minHeight = min(arr[i], arr[j])
                #print(' minHeight('+str(minHeight)+') = min(arr[i('+str(i)+')]='+str(arr[i])+', arr[j('+str(j)+')]='+str(arr[j]))
                for k in range(i, j):
                    #print(i,j,k)  
                    minHeight = min(minHeight, arr[k])
                    #print(' minHeight('+str(minHeight)+') = min(minHeight='+str(minHeight)+', arr[k('+str(k)+')]='+str(arr[k]))

                # calculate area using minHeight
                #  minHeight * width (distance between two columns)
                #print('  area : minHeight('+str(minHeight)+') ((j'+str(j)+' - i'+str(i)+') + 1)')                                
                #print('  area='+str(area))
                #print('  maxArea='+str(maxArea))
                area = ( minHeight * ((j - i) + 1) )
                maxArea = max(area,maxArea)
            #print('')

        print(maxArea)
    #\histogramArea()



    def histogramArea02(self,arr):
        print(arr)
        numBars = len(arr)
        maxArea=0

        # for all combinations
        for i in range(numBars):
            minHeight = arr[i]
            for j in range(i, numBars):
                # for all combinations of rectangles 
                #  determine the minHeight
                minHeight = min(minHeight, arr[j])

                # calculate area using minHeight
                #  minHeight * width (distance between two columns)
                area = ( minHeight * ((j - i) + 1) )

                #keep maxArea
                maxArea = max(area,maxArea)
            #\endfor
        #\endfor
        print(maxArea)        
    #\histogramArea02()




    def run(self):
        print("Run")

        #self.histogramArea([2,1,3,4,1])         #6
        #self.histogramArea([6,3,1,4,12,4])      #12
        #self.histogramArea([5,6,7,4,1])         #16     
        #self.histogramArea([2,2,2,2,16,2,2,2,2])#18      

        self.histogramArea02([2,1,3,4,1])         #6
        self.histogramArea02([6,3,1,4,12,4])      #12
        self.histogramArea02([5,6,7,4,1])         #16     
        self.histogramArea02([2,2,2,2,16,2,2,2,2])#18    

        print("Done")
    #\run()

#\PythonDevEnv

#run
print("Start")
pde = PythonDevEnv()
pde.run()