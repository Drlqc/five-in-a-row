# five-in-a-row
this reciprotary is just for our group to upload the file or some references you think are useful <br>
you can directly put the website link here

the original part of MCST we learn:https://github.com/zhuliquan/tictactoe_mcts

a new meaningful website https://ai-boson.github.io/mcts/, it clearly shows the structure of how to set the MCTS for 5-in-a-row game. you'd better see it carefully

##Li,Qichao
recently, I try some strategies<br>
1. I limit the span tree into the adjacent places so as to reduce the inefficient effort(since in five-in-a-row game, it almost useless to add piece remote from the existing nodes). As a result, the depth of the MCST increase to 3(used to be less than 2, the complexity is O($k^n$))
