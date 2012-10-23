%declare DIR '/production/userprofile/user_category_summary_merge_addrelation/subset/2012/10/01/p*';
A = load '/production/userprofile/user_category_summary_merge_addrelation/subset/2012/10/01/p*' as (pyid,cate_id:int,weight:float);
men = filter A by cate_id == 10110;
women = filter A by cate_id == 10111;
Coo = cogroup men by pyid, women by pyid;
#Gather = filter Coo by men is not null and women is not null;
result = foreach Coo generate flatten((IsEmpty(men)?null:men)),flatten((IsEmpty(women)?null:women));
split



