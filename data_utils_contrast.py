import json
def construct(score):
    text="user "+"rates "+str(score)+" "+"points "+"to "+"the book"
    return text

f1=open("train.txt")
f2=open("test.txt")
dict_line_all=[]
for line in f1:
    line=line.strip('\n').split('\t')
    userid=line[0]
    itemid=line[1]
    score=line[2]
    review=line[3]
    #print(userid,itemid,score,review)
    dict_line={}
    dict_line["reviewerID"]=userid
    dict_line["asin"]=itemid
    dict_line["overall"]=score
    dict_line["reviewText"]=review
    dict_line["summary"]=""
    dict_line_all.append(dict_line)

f1.close()
for line in f2:
    line=line.strip('\n').split('\t')
    userid=line[0]
    itemid=line[1]
    score=line[2]
    review=line[3]
    #print(userid,itemid,score,review)
    dict_line={}
    dict_line["reviewerID"]=userid
    dict_line["asin"]=itemid
    dict_line["overall"]=score
    dict_line["reviewText"]=review
    dict_line["summary"]=""
    dict_line_all.append(dict_line)
f2.close()
print(len(dict_line_all))


with open('./train1_contrast.json', 'w') as json_file:
    for each_dict in dict_line_all:
        json_file.write(json.dumps(each_dict)+'\n') 


f=open("train1_contrast.json")
review_dict={}
cnt=0
for line in f:
    line_dict=json.loads(line)
    cnt=cnt+1
    id=line_dict["reviewerID"]
    asin=line_dict["asin"]
    review=line_dict["reviewText"]
    score=line_dict["overall"]
    summary=line_dict["summary"]
    if id not in review_dict:
        review_dict[id]={}
        review_dict[id][score]={}
        review_dict[id][score][asin]={}
        review_dict[id][score][asin]["review"]=review
        review_dict[id][score][asin]["summary"]=summary
    else:
        if score not in review_dict[id]:
            review_dict[id][score]={}
            review_dict[id][score][asin]={}
            review_dict[id][score][asin]["review"]=review
            review_dict[id][score][asin]["summary"]=summary
        else:
            review_dict[id][score][asin]={}
            review_dict[id][score][asin]["review"]=review
            review_dict[id][score][asin]["summary"]=summary
f.close()

with open('./review_score_book_contrast.json', 'w') as json_file:
        json_file.write(json.dumps(review_dict))

f=open("train1_contrast.json")
book_dict={}
cnt=0
for line in f:
    line_dict=json.loads(line)
    cnt=cnt+1
    id=line_dict["reviewerID"]
    asin=line_dict["asin"]
    review=line_dict["reviewText"]
    score=line_dict["overall"]
    summary=line_dict["summary"]
    if asin not in book_dict:
        book_dict[asin]={}
        book_dict[asin][score]={}
        book_dict[asin][score][id]={}
        book_dict[asin][score][id]["review"]=review
        book_dict[asin][score][id]["summary"]=summary
    else:
        if score not in book_dict[asin]:
            book_dict[asin][score]={}
            book_dict[asin][score][id]={}
            book_dict[asin][score][id]["review"]=review
            book_dict[asin][score][id]["summary"]=summary
        else:
            book_dict[asin][score][id]={}
            book_dict[asin][score][id]["review"]=review
            book_dict[asin][score][id]["summary"]=summary
f.close()

with open('./book_score_reviewer_contrast.json', 'w') as json_file:
        json_file.write(json.dumps(book_dict))


f1=open("./review_score_book_contrast.json")
reviewer_dict=json.load(f1)
f1.close()
f2=open("./book_score_reviewer_contrast.json")
book_dict=json.load(f2)
f2.close()

f=open("train1_contrast.json")
dict_all=[]
dict_test=[]
cnt=1
for line in f:
    line_dict=json.loads(line)
    cnt=cnt+1
    reviewer_id=line_dict["reviewerID"]
    asin=line_dict["asin"]
    review=line_dict["reviewText"]
    score=str(line_dict["overall"])
    summary=line_dict["summary"]
    dict={}
    text_input=""
    book_text=""
    reviewer_style=""
    rate_text=construct(score)
    book_asin_score=book_dict[asin][score]
    book_cnt=0
    for id_tmp in book_asin_score:
        if id_tmp !=reviewer_id:
                book_text=book_text+book_dict[asin][score][id_tmp]["review"]
                book_cnt=book_cnt+1
        if book_cnt>3:
            break
    if book_text=="":
        book_text=summary
    review_id_score=reviewer_dict[reviewer_id][score]
    review_cnt=0
    for asin_tmp in review_id_score:
        if asin_tmp !=asin:
                reviewer_style=reviewer_style+reviewer_dict[reviewer_id][score][asin_tmp]["review"]
                review_cnt=review_cnt+1
        if review_cnt>3:
            break
    if reviewer_style=="" and book_text!=summary:
        reviewer_style=summary

    #拼接
    text_input=text_input+rate_text+";"+'\n'+book_text+";"+'\n'+reviewer_style+";"+'\n'
    
    
    dict['src']=text_input
    dict['tgt']=review
    if cnt%10==0:
        dict_test.append(dict)
    else:
        dict_all.append(dict)
    
    #先只在前80万个中拆训练和验证集
    if cnt>800000:
        break
f.close()


with open('./train1_contrast_trainset.json', 'w') as json_file:
    for each_dict in dict_all:
        json_file.write(json.dumps(each_dict)+'\n')

with open('./train1_contrast_testset.json', 'w') as json_file:
    for each_dict in dict_test:
        json_file.write(json.dumps(each_dict)+'\n')

