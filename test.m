a = zeros(2,2)
b = [3,7;5,8]

for i = 1:2
    a(i,:) = b(i,:);
end 

for i =1:2
    sum(a(i,:),2)
end 