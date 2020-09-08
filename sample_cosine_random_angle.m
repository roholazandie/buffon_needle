function [C] = sample_cosine_random_angle()

while 1
    u = 2 * rand() -1; %(-1, 1)
    v = rand(); %(0, 1)
    r = v * v + u * u;
    if r < 1
      break
    end
end

C = (u * u - v * v) / r;