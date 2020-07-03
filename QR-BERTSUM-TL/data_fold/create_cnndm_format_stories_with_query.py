import os
types=["train","valid","test"]
folds=[1,2,3,4,5,6,7,8,9,10]
path = os.getcwd()
path=path+"/"+"Debatepedia_With_Query_Stories_Fold_"
for fold in folds:
    create_directory=path+str(fold)
    os.mkdir(create_directory)
    for type in types:
        content=open(str(fold)+"/"+type+"_"+"content","r",encoding="utf-8")
        query = open(str(fold)+"/"+type+ "_" + "query", "r", encoding="utf-8")
        summary = open(str(fold)+"/"+type + "_" + "summary", "r", encoding="utf-8")
        n=0
        for (q,c,s) in zip(query,content,summary):
            n=n+1
            create_story=open(str(create_directory)+"/"+type+str(n)+".story","w+")
            create_story.write(q+"\n"+c+"\n"+"@highlight\n\n"+s+"\n")





