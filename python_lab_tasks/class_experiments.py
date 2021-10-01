import random
runs = 10
class Experiment:
    def __init__(self, num_runs, var=4):
        """
        init function just prints a message to standard output
        """
        self.num_runs = num_runs
        print("im alive")
        print("number of runs:", num_runs)
        print(var)
        

    def run_experiment(self):
        self.results = []
        for x in range(self.num_runs):
            n = random.random()
            self.results.append(n)
            
    def get_results(self):
        """
        Returns Results
        """
        return self.results

if __name__ == '__main__':
    an_experiment = Experiment(var=5,
                               num_runs=runs)
    an_experiment.run_experiment()
    results = an_experiment.get_results()
    print(results)
    print("")
    print(an_experiment.results)
