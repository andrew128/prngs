import matplotlib.pyplot as plt
import numpy as np
    
def get_samples_using_mcg(prime, multiplier, seed, num_samples):
    '''
    Get pseudorandom samples using a Multiplicative Congruential Generator.
    Gives a certain number of samples given a larger prime, 
    a multiplier, and a seed.
    '''
    output = [seed]
    
    previous_sample = seed
    for i in range(num_samples):
        r_i = (multiplier * previous_sample) % prime
        previous_sample = r_i
        output.append(r_i)

    return output

def get_uniform_continuous_samples(c, num_samples, prime=151,\
                                    multiplier=7, seed=1):
    '''
    Get uniform continuous samples between 0 and c using
    a Multiplicative Congurential Generator.
    '''
    samples = get_samples_using_mcg(prime, multiplier, seed, num_samples)
    uniform_samples = [(i/prime)*c for i in samples]
    return uniform_samples

def get_uniform_discrete_samples(c, num_samples, prime=151,\
                                    multiplier=7, seed=1):
    '''
    Get uniform discrete samples in [0, c) using
    a Multiplicative Congurential Generator.
    '''
    samples = get_samples_using_mcg(prime, multiplier, seed, num_samples)
    uniform_samples = [i%c for i in samples]
    return uniform_samples

def get_arbitrary_discrete_samples(num_samples, p = [0.1, 0.3, 0.2, 0.4],\
                                    prime=151, multiplier=7, seed=1):
    '''
    Input includes a probability distribution
    '''
    samples = get_samples_using_mcg(prime, multiplier, seed, num_samples)
    uniform_samples = [(i/prime) for i in samples]
    bucketed_samples = []

    for curr_sample in uniform_samples:
        prev_boundary = 0
        for j, bucket in enumerate(p):
            next_boundary = prev_boundary + bucket
            if curr_sample >= prev_boundary and curr_sample <= next_boundary:
                bucketed_samples.append(j)
                break

            prev_boundary = next_boundary

    return bucketed_samples

def main():
    # Uniform discrete
    uniform_discrete_samples = get_uniform_discrete_samples(6, 10000)
    plt.hist(uniform_discrete_samples, bins=6)
    plt.title('10000 Uniform Discrete Samples Between 0 and 5')
    plt.show()

    # Uniform continuous
    uniform_continuous_samples = get_uniform_continuous_samples(2, 10000)
    plt.hist(uniform_continuous_samples, bins=150)
    plt.title('10000 Uniform Continuous Samples Between 0 and 2')
    plt.show()

    # Arbitrary discrete
    arbitrary_discrete_samples = get_arbitrary_discrete_samples(10000)
    plt.hist(arbitrary_discrete_samples, bins=4)
    plt.title('10000 Arbitrary Discrete Samples')
    plt.show()

if __name__ == "__main__":
    main()