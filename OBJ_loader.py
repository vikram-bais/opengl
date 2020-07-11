import numpy as np
class OBJ:
    def load(filename):
        vertices=[]
        indices=[]
        ff=open(filename,"r")
        line=ff.readline()
        while line:
            string=str(line)
            line = ff.readline()
            line_list=string.split(" ")
            if line_list[0]=="#":
                continue
            elif line_list[0]=="v":
                tempver=[]
                tempver.append(float(line_list[1]))
                tempver.append(float(line_list[2]))
                tempver.append(float(line_list[3]))
                vertices.append(tempver)
            elif line_list[0]=="f":
                for ele in range(1,4):
                    lll=line_list[ele].split("/")
                    indices.append(int(lll[0]))
            else:
                continue
        ff.close()
        indices=np.array(indices)
        indices=indices.reshape(-1,3)
        return vertices,indices