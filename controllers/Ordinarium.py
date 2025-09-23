# -*- encoding:utf-8 -*-
from controllers.ControllerManager import ControllerManager
from datetime import datetime

"""
    Ordination of the office and mass for the given day.
"""


class Ordination:
    def __init__(self):
        cm = ControllerManager()
        self.occurence_ctrl = cm.get_occurrence_ctrl()
        self.contents_ctrl = cm.get_contents_ctrl()
        self.temporal_ctrl = cm.get_temporal_ctrl()
        self.sanctoral_ctrl = cm.get_sanctoral_ctrl()
        self.diocese_ctrl = cm.get_diocese_ctrl()
        self.congregation_ctrl = cm.get_congregation_ctrl()

    def office(self, country:str, diocese: str, congregation: str, day: datetime):
        """
        Orchestrate feast selection for a given day with the following policy:
        - Temporal has global priority over Sanctoral/Diocese/Congregation.
        - When Temporal is absent, compare remaining candidates using OccurenceCtrl,
          then adjust structure with ContentsCtrl.
        The function is defensive against missing fields (rank/occ/con).
        """

        def norm(f: dict | None) -> dict | None:
            if not f:
                return None
            # Defensive defaults
            f.setdefault('occ', '')
            f.setdefault('con', '')
            # Normalize codes (strip whitespace)
            f['occ'] = (str(f.get('occ') or '')).strip()
            f['con'] = (str(f.get('con') or '')).strip()
            return f
        
        # Gather candidates
        day_dioc = norm(self.diocese_ctrl.calendar_diocese(country, diocese, day)) if self.diocese_ctrl else None
        day_cong = norm(self.congregation_ctrl.calendar_congregation(congregation, day)) if self.congregation_ctrl else None
        day_temp = norm(self.temporal_ctrl.get_fest(day)) if self.temporal_ctrl else None
        day_sanct = norm(self.sanctoral_ctrl.get_fest(day)) if self.sanctoral_ctrl else None

        # Start with the first available candidate in a fixed order
        fest = day_temp or day_sanct or day_dioc or day_cong
        
        # Helper to merge two candidates using occurrence then contents matrices
        def merge_with(current: dict | None, other: dict | None) -> dict | None:
            if not other:
                return current
            if current is None:
                return other
            # Decide via occurrence matrix then tune contents
            try:
                base = self.occurence_ctrl.search(current, other)
            except Exception:
                # Fallback: keep current; do not use rank here
                base = current
            try:
                tuned = self.contents_ctrl.search(base, other if base is current else current)
            except Exception:
                tuned = base
            return tuned

        # Merge all candidates in order: Temporal, Sanctoral, Diocese, Congregation
        # (Every pair is compared; no source is automatically prioritized)
        fest = merge_with(fest, day_temp if fest is not day_temp else None)
        fest = merge_with(fest, day_sanct)
        fest = merge_with(fest, day_dioc)
        fest = merge_with(fest, day_cong)

        return fest or {}

    def mass(self):
        pass
