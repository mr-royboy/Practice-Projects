{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "3e4c1a3c-98fd-4899-b409-51435f4d6e06",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "suits = (\"Hearts\", \"Diamonds\", \"Spades\", \"Clubs\")\n",
    "ranks = (\"Two\", \"Three\", \"Four\", \"Five\", \"Six\", \"Seven\", \"Eight\", \"Nine\", \"Ten\", \"Jack\", \"Queen\", \"King\", \"Ace\")\n",
    "values = {\"Two\" : 2, \"Three\" : 3, \"Four\" : 4, \"Five\" : 5, \"Six\" : 6, \"Seven\" : 7, \"Eight\" : 8, \"Nine\" : 9, \"Ten\" : 10, \"Jack\" : 11, \"Queen\" : 12, \"King\" : 13, \"Ace\" : 14}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "2fac1a34-3bb2-4ce9-a9b2-5d639dc560e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Card:\n",
    "\n",
    "    def __init__(self, suit, rank):\n",
    "\n",
    "        self.suit = suit\n",
    "        self.rank = rank\n",
    "        self.value = values[rank]\n",
    "\n",
    "    def __str__(self):\n",
    "\n",
    "        return self.rank + \" of \" + self.suit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "0787decd-c941-45e0-af9b-ff050a4a07b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "two_hearts = Card(\"Heart\", \"Two\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "020536bd-432e-4eb0-9716-5d5f74dd2594",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Card at 0x1b4eee6a840>"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "two_hearts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "7e4ea60d-7014-4945-9e0e-8fdd25c68c8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Two of Heart\n"
     ]
    }
   ],
   "source": [
    "print(two_hearts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "7be3fdbf-6824-4984-9964-5c869f247bb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Deck:\n",
    "\n",
    "    def __init__(self):\n",
    "\n",
    "        # selecting all the cards in a deck\n",
    "        self.all_cards = []\n",
    "\n",
    "        for suit in suits:\n",
    "            for rank in ranks:\n",
    "\n",
    "                created_card = Card(suit, rank)\n",
    "\n",
    "                self.all_cards.append(created_card)\n",
    "\n",
    "    def shuffle(self):\n",
    "\n",
    "        # shuffling all the cards\n",
    "        random.shuffle(self.all_cards)\n",
    "\n",
    "    def deal_one(self):\n",
    "\n",
    "        # takes and pops out a card out of the deck\n",
    "        return self.all_cards.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "96497013-4291-4cb7-8ac1-58e880c0883a",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_deck = Deck()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "d8bce23a-a42a-4ebb-8756-c1784950728b",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_deck.shuffle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "405a87e7-386a-40c4-a10f-92043b425e44",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_card = new_deck.deal_one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "b6fe36b4-d653-4491-aa1a-c967f529c47b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Four of Diamonds\n"
     ]
    }
   ],
   "source": [
    "print(my_card)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "3aed937b-6590-40fc-92d9-e97d4f1a6f7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "51"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(new_deck.all_cards)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "fbeef888-2990-420b-a75e-441fcd6b74de",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Player:\n",
    "\n",
    "    def __init__(self, name):\n",
    "\n",
    "        self.name = name\n",
    "        self.all_cards = []\n",
    "\n",
    "    def remove_one(self):\n",
    "        # pops one out of the deck\n",
    "        return self.all_cards.pop(0)\n",
    "\n",
    "    def add_cards(self, new_cards):\n",
    "        \n",
    "        if type(new_cards) == type([]):\n",
    "\n",
    "            # list of multiple cards object\n",
    "            self.all_cards.extend(new_cards)\n",
    "\n",
    "        else:\n",
    "\n",
    "            # for a single card object\n",
    "            self.all_cards.append(new_cards)\n",
    "\n",
    "    def __str__(self):\n",
    "        return f\"Player {self.name} has {len(self.all_cards)} cards.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "839e5650-22b2-4946-8343-ad9126804b22",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_player = Player(\"Roy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "f73bc879-91c0-4d9d-9339-ba2ab55a2413",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player Roy has 0 cards.\n"
     ]
    }
   ],
   "source": [
    "print(new_player)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "0b8fdb7b-b70e-46d0-95c9-6c729361edfc",
   "metadata": {},
   "source": [
    "new_player.add_cards(my_card)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "31ed3d84-3538-49dc-97fb-9a503df13d02",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Player at 0x1b4ee8b1970>"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_player"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "735bd165-2489-4ab3-93d1-db8e3f22faf1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player Roy has 0 cards.\n"
     ]
    }
   ],
   "source": [
    "print(new_player)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "2be2f9b1-5dcc-4a97-bdc1-ac91fbe2d328",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Four of Diamonds\n"
     ]
    }
   ],
   "source": [
    "print(my_card)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "412c2205-b613-4812-8056-74fc88d7f053",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player Roy has 0 cards.\n"
     ]
    }
   ],
   "source": [
    "print(new_player)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "62d60214-f6b6-4735-81c1-6d5d95dd944e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# GAME SETUP\n",
    "\n",
    "player_one = Player(\"One\")\n",
    "player_two = Player(\"Two\")\n",
    "\n",
    "new_deck = Deck()\n",
    "new_deck.shuffle()\n",
    "\n",
    "for x in range(26):\n",
    "\n",
    "    player_one.add_cards(new_deck.deal_one())\n",
    "    player_two.add_cards(new_deck.deal_one())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "baa17541-4129-4ebf-a8b0-91387b182fac",
   "metadata": {},
   "outputs": [],
   "source": [
    "game_on = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "68626290-5376-4c0d-80ae-dc2430c36fad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Round 1\n",
      "Round 2\n",
      "Round 3\n",
      "Round 4\n",
      "Round 5\n",
      "Round 6\n",
      "Round 7\n",
      "Round 8\n",
      "Round 9\n",
      "Round 10\n",
      "Round 11\n",
      "Round 12\n",
      "Round 13\n",
      "War!\n",
      "Round 14\n",
      "Round 15\n",
      "Round 16\n",
      "Round 17\n",
      "Round 18\n",
      "Round 19\n",
      "Round 20\n",
      "Round 21\n",
      "Round 22\n",
      "Round 23\n",
      "Round 24\n",
      "Round 25\n",
      "Round 26\n",
      "Round 27\n",
      "Round 28\n",
      "Round 29\n",
      "Round 30\n",
      "Round 31\n",
      "Round 32\n",
      "Round 33\n",
      "Round 34\n",
      "Round 35\n",
      "Round 36\n",
      "Round 37\n",
      "Round 38\n",
      "Round 39\n",
      "Round 40\n",
      "Round 41\n",
      "Round 42\n",
      "Round 43\n",
      "Round 44\n",
      "Round 45\n",
      "Round 46\n",
      "Round 47\n",
      "Round 48\n",
      "Round 49\n",
      "Round 50\n",
      "War!\n",
      "Round 51\n",
      "Round 52\n",
      "Round 53\n",
      "Round 54\n",
      "Round 55\n",
      "Round 56\n",
      "Round 57\n",
      "Round 58\n",
      "Round 59\n",
      "Round 60\n",
      "Round 61\n",
      "Round 62\n",
      "Round 63\n",
      "Round 64\n",
      "Round 65\n",
      "Round 66\n",
      "Round 67\n",
      "Round 68\n",
      "Round 69\n",
      "Round 70\n",
      "Round 71\n",
      "Round 72\n",
      "Round 73\n",
      "Round 74\n",
      "Round 75\n",
      "Round 76\n",
      "Round 77\n",
      "Round 78\n",
      "Round 79\n",
      "Round 80\n",
      "War!\n",
      "Round 81\n",
      "Round 82\n",
      "Round 83\n",
      "War!\n",
      "Round 84\n",
      "Round 85\n",
      "Round 86\n",
      "Round 87\n",
      "Round 88\n",
      "Round 89\n",
      "Round 90\n",
      "Round 91\n",
      "Round 92\n",
      "Round 93\n",
      "Round 94\n",
      "Round 95\n",
      "Round 96\n",
      "Round 97\n",
      "Round 98\n",
      "Round 99\n",
      "Round 100\n",
      "Round 101\n",
      "Round 102\n",
      "Round 103\n",
      "War!\n",
      "Round 104\n",
      "Round 105\n",
      "Round 106\n",
      "Round 107\n",
      "Round 108\n",
      "Round 109\n",
      "Round 110\n",
      "Round 111\n",
      "Round 112\n",
      "Round 113\n",
      "Round 114\n",
      "Round 115\n",
      "Round 116\n",
      "Round 117\n",
      "Round 118\n",
      "Round 119\n",
      "Round 120\n",
      "Round 121\n",
      "Round 122\n",
      "Round 123\n",
      "Round 124\n",
      "Round 125\n",
      "Round 126\n",
      "Round 127\n",
      "Round 128\n",
      "War!\n",
      "Round 129\n",
      "Round 130\n",
      "Round 131\n",
      "Round 132\n",
      "Round 133\n",
      "Round 134\n",
      "Round 135\n",
      "Round 136\n",
      "Round 137\n",
      "War!\n",
      "Round 138\n",
      "Round 139\n",
      "Round 140\n",
      "War!\n",
      "Round 141\n",
      "Round 142\n",
      "Round 143\n",
      "Round 144\n",
      "Round 145\n",
      "Round 146\n",
      "Round 147\n",
      "Round 148\n",
      "Round 149\n",
      "Round 150\n",
      "Round 151\n",
      "Round 152\n",
      "Round 153\n",
      "Round 154\n",
      "Round 155\n",
      "Round 156\n",
      "Round 157\n",
      "Round 158\n",
      "Round 159\n",
      "Round 160\n",
      "Round 161\n",
      "Round 162\n",
      "Round 163\n",
      "Round 164\n",
      "Round 165\n",
      "Round 166\n",
      "Round 167\n",
      "Round 168\n",
      "Round 169\n",
      "Round 170\n",
      "Round 171\n",
      "Round 172\n",
      "Round 173\n",
      "Round 174\n",
      "Round 175\n",
      "Round 176\n",
      "Round 177\n",
      "Round 178\n",
      "Round 179\n",
      "Round 180\n",
      "Round 181\n",
      "Round 182\n",
      "Round 183\n",
      "Round 184\n",
      "Round 185\n",
      "Round 186\n",
      "Round 187\n",
      "Round 188\n",
      "Round 189\n",
      "Round 190\n",
      "War!\n",
      "Round 191\n",
      "Round 192\n",
      "Round 193\n",
      "Round 194\n",
      "Round 195\n",
      "Round 196\n",
      "Round 197\n",
      "Round 198\n",
      "Round 199\n",
      "Round 200\n",
      "Round 201\n",
      "War!\n",
      "Round 202\n",
      "Round 203\n",
      "Round 204\n",
      "Round 205\n",
      "Round 206\n",
      "War!\n",
      "Round 207\n",
      "Round 208\n",
      "Round 209\n",
      "Round 210\n",
      "Round 211\n",
      "Round 212\n",
      "Round 213\n",
      "Round 214\n",
      "Round 215\n",
      "Round 216\n",
      "Round 217\n",
      "War!\n",
      "Round 218\n",
      "Round 219\n",
      "War!\n",
      "Round 220\n",
      "Round 221\n",
      "Round 222\n",
      "Round 223\n",
      "Round 224\n",
      "Round 225\n",
      "Round 226\n",
      "Round 227\n",
      "Round 228\n",
      "War!\n",
      "Round 229\n",
      "Round 230\n",
      "Round 231\n",
      "Round 232\n",
      "Round 233\n",
      "Round 234\n",
      "Round 235\n",
      "Round 236\n",
      "Round 237\n",
      "Round 238\n",
      "Round 239\n",
      "Round 240\n",
      "Round 241\n",
      "Round 242\n",
      "War!\n",
      "Round 243\n",
      "Round 244\n",
      "Round 245\n",
      "War!\n",
      "Player Two unable to declare War.\n",
      "Player One WINS!\n"
     ]
    }
   ],
   "source": [
    "round_num = 0\n",
    "\n",
    "while game_on:\n",
    "\n",
    "    round_num += 1\n",
    "    print(f\"Round {round_num}\")\n",
    "\n",
    "    if len(player_one.all_cards) == 0:\n",
    "        print(\"Player One is out of cards! Player Two wins!\")\n",
    "        game_on = False\n",
    "        break\n",
    "\n",
    "    if len(player_two.all_cards) == 0:\n",
    "        print(\"Player Two is out of cards! Player One Wins!\")\n",
    "        game_on = False\n",
    "        break\n",
    "\n",
    "    # START A NEW ROUND\n",
    "\n",
    "    # these two variables are NOT SAME as player_one.all_cards, it is more like cards in player's play. \n",
    "    player_one_cards = []\n",
    "    # to start a new round, we append card(s) from .all_cards\n",
    "    player_one_cards.append(player_one.remove_one())\n",
    "    \n",
    "    player_two_cards = []\n",
    "    player_two_cards.append(player_two.remove_one())\n",
    "\n",
    "    at_war = True\n",
    "\n",
    "    while at_war:\n",
    "\n",
    "        # checking from the last card because checking from the first would keep it in loop\n",
    "        if player_one_cards[-1].value > player_two_cards[-1].value:\n",
    "\n",
    "            # after winning the war, player one collects the cards of both the players\n",
    "            player_one.add_cards(player_one_cards)\n",
    "            player_one.add_cards(player_two_cards)\n",
    "\n",
    "            at_war = False\n",
    "            # the game ends while at war and begins from while game_on\n",
    "\n",
    "        elif player_one_cards[-1].value < player_two_cards[-1].value:\n",
    "\n",
    "            player_two.add_cards(player_two_cards)\n",
    "            player_two.add_cards(player_one_cards)\n",
    "\n",
    "            at_war = False\n",
    "            # the game ends while at war with player two winning the round and begins again from while game_on\n",
    "\n",
    "        else:\n",
    "            print(\"War!\")\n",
    "\n",
    "            if len(player_one.all_cards) < 3:\n",
    "\n",
    "                print(\"Player One unable to declare War.\")\n",
    "                print(\"Player Two WINS!\")\n",
    "                game_on = False\n",
    "                break\n",
    "\n",
    "            elif len(player_two.all_cards) < 3:\n",
    "\n",
    "                print(\"Player Two unable to declare War.\")\n",
    "                print(\"Player One WINS!\")\n",
    "                game_on = False\n",
    "                break\n",
    "\n",
    "            else:\n",
    "\n",
    "                for num in range(3):\n",
    "\n",
    "                    player_one_cards.append(player_one.remove_one())\n",
    "                    player_two_cards.append(player_two.remove_one())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1bc6b27-9032-4657-bb1c-095b8df7e769",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60211394-4e79-4cae-890b-ea8a2a924532",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
