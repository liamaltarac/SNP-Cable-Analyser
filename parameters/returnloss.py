from parameter import Parameter, complex2db

class ReturnLoss(Parameter):
    def computeParameter(self):
        # initialize the dictionary for each port
        rl = dict()
        for port in self._ports:
            rl[port] = list()


        # extract the return loss in all matrices
        for (f,_) in enumerate(self._freq):
            for (i,port) in self._ports.items():
                # get the value
                value = self._matrices[f, i, i]

                # convert to db if specified
                if self._complex:
                    value = complex2db(value)

                # add the value to the list
                rl[port].append(value)

        return rl
