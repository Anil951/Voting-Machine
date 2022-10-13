## Voting-Machine ##
***
* A simple voting machine where a voter votes to the candidate of his choice.
* This Project main aim is to provide safe and secure voting system environment, where
admin can allow the user to vote, and admin declare a result.

1. Project is people to vote and select their Leader
2. Project may be used colleges / schools to select Class Representative or Leader to
college
3. Simple to Use and May Future need this
4. Voting does not to be scam. This project is safe and secure.

* Here, there are 2 scenarios where voter can vote,
   1. if the name of voter is there in list(signup.csv),then to vote first he must go through sign in and proceed to vote.
   2. if the name is not there in the list(signup.csv),then to vote he must create a username & password by clicking sign-up option and proceed to vote by signin.
* In my machine a voter can vote to any of the candidate only once,this is encrypted by the 't/f' element in the list(signup.csv).if the voter has used his vote option      then his name is saved in the list as 't',in the opposite case it will be 'f',
* If the user created credentials by using signup option does not use cast-vote option then,it will be considered as duplicate user and his details will not be stored in the list(signup.csv).
* Live count is also shown to the voter from the deatils stored in file-(votecount.csv).
* signup.csv model:

    | Username  | Password  | t/f |
    | :-----------: |:---------------:| :----:|
    | voter 1 name  | voter 1 pass  | t/f |
    | voter 2 name  | voter 2 pass  | t/f |

* votevount.csv model:

    | vote count of canditate 1  | vote count of canditate 2  | vote count of canditate 3 | vote count of canditate 4  | vote count of canditate 5 |
    | :-----------: |:---------------:| :------------:| :-----------: |:---------------:|

* There by,providing a safe atmosphere of an election to the voter 😄
