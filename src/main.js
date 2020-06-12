import notify from './Notification';

require('./main.css');
notify.log('Here is the message again');
notify.announce('Here is my message');

class Form {
    constructor() {
        let numbers = [5, 10, 15].map(number => number * 2);
        console.log(numbers);
    }
}

new Form();