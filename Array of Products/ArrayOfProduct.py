
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftCurrentProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftCurrentProduct
        leftCurrentProduct = leftCurrentProduct  * array[i]

    rightCurrentProduct = 1
    for i in  reversed(range(len(array))):
        rightProducts[i] = rightCurrentProduct
        rightCurrentProduct = rightCurrentProduct * array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products



# OR By Dividing Current Element

def arrayOfProductsByDivision(array):
    products = 1
    for i in array:
        products *= i

    ans = [1 for _ in range(len(array))]
    j=0
    for i in array:
        ans[j] = products//i
        j+=1
    return ans


array = [1,2,3,4]
x = arrayOfProducts(array)
print(x)
x=arrayOfProductsByDivision(array)
print(x)

