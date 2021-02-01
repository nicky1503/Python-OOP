from defining_classes.guild_system_7.project.player import Player
from typing import List

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_to_kick = [p for p in self.players if p.name == player_name]
        if not player_to_kick:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player_to_kick[0])
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players:
            result += p.player_info()
        return result

