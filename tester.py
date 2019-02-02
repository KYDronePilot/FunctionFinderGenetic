from function_finder import Main


if __name__ == '__main__':
    found = False
    while not found:
        main = Main()
        # Load in from config file.
        main.load_attributes()
        # Configure the Equation Tree class.
        main.configure_equation_tree()
        # Start the nucleus.
        main.init_nucleus()
        # Evolve.
        rc = main.evolve()
        # Print message declaring whether an ideal individual was found or not.
        if rc:
            print('An ideal individual was found.')
            found = True
        else:
            print('No ideal individual was found.')
        # Print the best individual.
        main.nucleus.sort()
        print('Error: ', main.nucleus.population[0].error)
        print(main.nucleus.population[0].equation.render())
        main.nucleus.plot_learning()
