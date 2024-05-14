"""
Common to all rule systems
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union, cast

class RulesSpec:
    """
    A rule consists of
    - closed intervals of levels for which it is relevant
    - a number indicating which precedence it should have when printing
        out the rules rules_text for the given level
    - the text to print out
    """
    def __init__(self, levels : Union[int,Tuple[int,int],List[Tuple[int,int]]],
                 upper_bound_levels: int,
                 sort_order: int,
                 rules_text: str):
        if isinstance(levels,int):
            self.level_intervals = [(levels,upper_bound_levels)]
        elif isinstance(levels,tuple):
            self.level_intervals = [levels]
        else:
            self.level_intervals = levels
        self.sort_order = sort_order
        self.rules_text = rules_text

    def relevant_at_this_level(self,level) -> bool:
        """
        does this rule go into the printed rules when at this level
        """
        for interval in self.level_intervals:
            cur_int_min, cur_int_max = interval
            if cur_int_min<=level<=cur_int_max:
                return True
        return False

    @staticmethod
    def parse(raw : Dict[str,Any], upper_bound_levels : int = 200) -> RulesSpec:
        """
        from an unstructured key value store
        """
        rule_level = cast(Optional[int],raw.get("level",None))
        if rule_level is not None:
            my_levels = rule_level
        else:
            rule_level_range = cast(Optional[Tuple[int,int]],raw.get("level_range",None))
            if rule_level_range is not None:
                my_levels = rule_level_range
            else:
                raise TypeError("""raw should have either
                                a level of rules level
                                which are integer or pair of integers respectively""")
        return RulesSpec(my_levels,
                 upper_bound_levels,
                 raw.get("sort_order",0),
                 raw.get("text",""))


def display_the_rules(all_rules : List[RulesSpec], cur_level: int) -> str:
    """
    the rules text at current level
    """
    relevant_rules = sorted(
        filter(lambda r: r.relevant_at_this_level(cur_level),all_rules),
        key = lambda r: r.sort_order,
        reverse = True)
    return "\n\n".join(map(lambda r: r.rules_text.strip(), relevant_rules))
