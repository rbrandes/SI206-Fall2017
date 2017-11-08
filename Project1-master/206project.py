import os
import filecmp
import datetime

#worked with ava weiner and aly rosenberg: did code seperately and then checked over for errors
#name:rachel brandes				

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	f=open(file,"r")
	data=[line.strip().split(',') for line in f.readlines()]
	titles = data[0]
	final=[]
	for person in data[1:]:
		dic={}
		dic[titles[0]]=person[0] #firstname
		dic[titles[1]]=person[1] #last name
		dic[titles[2]]=person[2] #email
		dic[titles[3]]=person[3] #class
		dic[titles[4]]=person[4] #DOB
		final.append(dic)
	return final

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	values=[]
	for x in data:
		 values.append(x[col])
	values2= sorted(values)
	person=values2[0]
	for x in data:
		if x[col] is person:
			return x['First'] + ' ' + x['Last']




#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g fri
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	Classes={'Senior':0, 'Junior':0, 'Freshman':0, 'Sophomore':0}
	for x in data:
		if x['Class'] == 'Senior':
			Classes['Senior'] += 1
		elif x['Class'] == 'Junior':
			Classes['Junior'] += 1
		elif x['Class'] == 'Freshman':
			Classes['Freshman'] += 1
		elif x['Class'] == 'Sophomore':
			Classes['Sophomore'] += 1
	Sorted_Classes=sorted(Classes, key=lambda x:Classes[x],reverse=True)
	Class_Totals=[]
	for x in Sorted_Classes:
		Class_Totals.append((x,Classes[x]))
	return Class_Totals


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	Days={}
	for x in a:
		date=x['DOB'].split('/')
		day=date[1]
		if day not in Days:
			Days[day]=1
		else:
			Days[day]+=1
	Sorted_Days=sorted(Days, key=lambda x:Days[x], reverse=True)
	return int(Sorted_Days[0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	Birth_Date=[]
	for person in a[1:]:
		birth_month, birth_day, birth_year = person ['DOB'].split('/')
		current_year=int(datetime.date.today().year)
		current_month=int(datetime.date.today().month)
		current_day=int(datetime.date.today().day)
		if ((current_day > int(birth_day)) and (current_month > int(birth_month))):
			Birth_Date.append(current_year-int(birth_year))
		else:
			Birth_Date.append(current_year-int(birth_year)+1)
	return round ((sum(Birth_Date)/len(Birth_Date)),0)


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	new_file = open(fileName, "w")
	sorted_data = sorted(a, key= lambda k: k[col])
	for item in sorted_data:
		items=[]
		for x in item.values():
			items.append(x)
		line=",".join(items[:3])
		new_file.write(line+"\n")

	new_file.close()
	return None

	



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

