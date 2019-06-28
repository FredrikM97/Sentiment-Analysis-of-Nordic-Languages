function result = stats(x)

xSize = size(x,2);
result = zeros(7,xSize);
for loop = 1:xSize
    result(1,loop) = max(x(:,loop));	%Maximum value
    result(2,loop) = mean(x(:,loop));	%Average or mean value
    result(3,loop) = median(x(:,loop));	%Median value
    result(4,loop) = min(x(:,loop)); 	%Smallest value
    result(5,loop) = mode(x(:,loop));	%Most frequent value
    result(6,loop) = std(x(:,loop)); 	%Standard deviation
    result(7,loop) = var(x(:,loop));  	%Variance, the spread or dispersion of the values
end
end
