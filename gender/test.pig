%declare DIR '*';
men = filter A by cate_id == 10110;
women = filter A by cate_id == 10111;
Coo = cogroup men by pyid, women by pyid;
#Gather = filter Coo by men is not null and women is not null;
result = foreach Coo generate flatten((IsEmpty(men)?null:men)),flatten((IsEmpty(women)?null:women));
split



