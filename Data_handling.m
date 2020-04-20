%�������� ��� ������������ �� ������. �������: �������, ������: ������.
%������� import ��� ������ 1,2,3 ��� �� ������ u.data ��� ������ data.
a = max(data(:,1));
b = max(data(:,2));
U = zeros(a,b);
for i = 1:size(data,1)
    U(data(i,1),data(i,2)) = data(i,3);
end

%�������� ��� ������������ ��� ������.
I = eye(a);

%���������� �� ������.
writematrix(I,'Input.csv');
writematrix(U,'Output.csv');

%����������� ��� ���������.
[m,n] = size(U);
A = zeros(m,n);
for i = 1:m
    count = 0;
    sum = 0;
    for j = 1:n
        if U(i,j)~=0
            count = count +1;
            sum = sum + U(i,j);
        end
    end
    mo = sum/count;
    
    for j = 1:n
        if U(i,j)~=0
            A(i,j) = U(i,j) - mo;
        end
    end
end
writematrix(A,'Output(centered).csv');

%���������� ������� ����� �� ������ ����.
[m,n] = size(U);
B = zeros(m,n);
for i = 1:m
    for j = 1:n
        if U(i,j) == 0
            B(i,j) = randi([1 5]);
        else
            B(i,j) = U(i,j);
        end
    end
end
writematrix(B,'Output(completed-random).csv');

%�����������.
D = zeros(m,n);
for i = 1:m
    count = 0;
    sum = 0;
    for j = 1:n
        if B(i,j)~=0
            count = count +1;
            sum = sum + B(i,j);
        end
    end
    mo = sum/count;
    
    for j = 1:n
        if B(i,j)~=0
            D(i,j) = B(i,j) - mo;
        end
    end
end
writematrix(D,'Output(completed-random-centered).csv');

%���������� ������� ����� �� �� ���� ���� ��� ����������� �����������.
C = zeros(m,n);
for i = 1:m
    count = 0;
    sum = 0;
    for j = 1:n
        if U(i,j)~=0
            count = count +1;
            sum = sum + U(i,j);
        end
    end
    mo = sum/count;
    
    for j = 1:n
        if U(i,j) == 0
            C(i,j) = mo;
        else
            C(i,j) = U(i,j);
        end
    end
end
writematrix(C,'Output(completed-mo).csv');

%�����������.
E = zeros(m,n);
for i = 1:m
    count = 0;
    sum = 0;
    for j = 1:n
        if C(i,j)~=0
            count = count +1;
            sum = sum + C(i,j);
        end
    end
    mo = sum/count;
    
    for j = 1:n
        if C(i,j)~=0
            E(i,j) = C(i,j) - mo;
        end
    end
end
writematrix(E,'Output(completed-mo-centered).csv');