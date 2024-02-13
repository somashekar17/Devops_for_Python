#Data structure is a organization of data in a one place.
#List for devops
list_of_cloud=["AWS","Azure","GCP","Oracle"]
# print(type(list_of_num))

# print(list_of_num[1])
for cloud in list_of_cloud:
    if cloud == "AWS":
        print("aws is best", cloud)
    else:
        print("Cloud not AWS:", cloud)

#dictionary for devops

dict_of_cloud={
    "aws":"Amazon web services",
    "azure":"Microsoft Azure",
    "GCP":"Google cloud platform"
}
print(dict_of_cloud)
print(dict_of_cloud["aws"])
print(dict_of_cloud.get("aws"))
dict_of_cloud.update({"Linode":"hh"})
print(dict_of_cloud)