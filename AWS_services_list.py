#Create a list of AWS services
#Project Requirements:

#1. The list should be empty initially.
#2. Populate the list using append or insert.
#3. Print the list and the length of the list.
#4. Remove two specific services from the list by name or by index.
#5. Print the new list and the new length of the list.

List = []

List.append('S3') 
List.append('DynamoDB')
List.append('EC2') 
List.append('Lambda')
List.append('CodePipeline')

print("Top 5 AWS Services:", List)

List_length = str(len(List))
print("# of Available Services:", List_length)

del List[3:5]
print("Top 3 AWS Services", List)

List_length = str(len(List))
print("# of Available Services:", List_length)