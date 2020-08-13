def getRow(rowIndex):
    row = [1]
    if rowIndex == 0:
        return row
    else:
        row.append(1)
        if rowIndex == 1:
            return row
        else:
            while len(row)<=rowIndex:
                newrow=row.copy()
                newrow.append(1)
                for i in range(1,len(row)):
                    newrow[i]=row[i-1]+row[i]
                row = newrow.copy()
            return row