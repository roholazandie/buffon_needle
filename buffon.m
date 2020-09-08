clc;
clear;

n_simulations = 10;
n_throws = 8000000;
strip_width = 2;
needle_width = 1;

estimates = zeros(1, n_simulations);
for i=1:n_simulations
    n_hits = 0;
    for j=1:n_throws
        needle_center = rand() * strip_width;
        C = sample_cosine_random_angle();
        
        if needle_center + C * needle_width/2 >= strip_width || needle_center - C * needle_width/2 <= 0
            n_hits = n_hits + 1;
        end       
    end
    estimates(i)= needle_width/strip_width * n_throws / n_hits;
end