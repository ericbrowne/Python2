clear all;
close all;

A= [0,0.0043,0.1132,0;
    0.9775,0.9111,0,0;
    0,0.0736,0.9534,0;
    0,0,0.0452,0.9804];
A;

% Part a)
eigenvalues = eig(A);
dominant_eigenvalue = eigenvalues(2); % the dominant eigen value is 1.0254
[V,D] = eig(A) %This is how we get w
w = V(5:8) %This is the w


%Part b)
x_0=[10,60,110,70];
C = (x_0)*((A)^50); %This is the 50th year

%Part c)

%set up population matrix:
population = zeros(50,4);
population_sum= zeros(50,1);
population_growthrate = zeros(50,1);

for i = 1:50
    population(i,:)=(x_0)*((A)^i);
    
end
population;

% sum those populations
population_sum = sum(population,2);

% Calculate the population growth rate for each year
for i = 1:49
    population_growthrate(i) = (population_sum(i+1)/ population_sum(i));
end 

% End case:
population_growthrate(50) = (population_sum(50)/population_sum(49));
B = 1:50;  % A 1-50 vector



%Calculate proportions:
yearlings_pop = zeros(50,1);
juveniles_pop = zeros(50,1);
mature_pop = zeros(50,1);
postreproductive_pop = zeros(50,1);
yearlings_proportion = zeros(50,1);
juveniles_proportion = zeros(50,1);
mature_proportion = zeros(50,1);
postreproductive_proportion = zeros(50,1);

for i = 1:50
    yearlings_pop(i) = population(i,1);
    juveniles_pop(i) = population(i,2);
    mature_pop(i) = population(i,3);
    postreproductive_pop(i) = population(i,4);
end

for i =1:50
    yearlings_proportion(i) = yearlings_pop(i)/population_sum(i);
    juveniles_proportion(i) = juveniles_pop(i)/population_sum(i);
    mature_proportion(i) = mature_pop(i)/population_sum(i);
    postreproductive_proportion(i) = postreproductive_pop(i)/population_sum(i);
end 

%%%%%%%%%%     Total population     %%%%%%%%%%%%
figure(1)
plot(B,population_sum)
grid
title('Total population for each of the next 50 years')
xlabel('Time')
ylabel('Total Population')

%%%%%%%%%%      Population Growth Rate      %%%%%%%%%%%
figure(2)
plot(B,population_growthrate)
grid
title('Total Population Growth Rate over the next 50 years')
xlabel('Time')
ylabel('Population Growth Rate')


%%%%%%%%%%% Proportions of individualts at each stage %%%%%%%%%%%%%%%%
figure(3)
plot(B,yearlings_proportion)
hold on
plot(B,juveniles_proportion)
hold on
plot(B,mature_proportion)
hold on
plot(B,postreproductive_proportion)
hold off
grid
title('Proportions of individuals at each stage for each year')
xlabel('Time in years')
ylabel('Proportion to total population')


