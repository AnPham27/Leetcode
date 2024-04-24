/**
Submitted: April 24, 2024
Question: Write a function argumentsLength that returns the count of arguments passed to it.
 */

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};
