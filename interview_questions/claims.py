from collections import defaultdict
from typing import List, Dict

def count_claims_by_region(claims: List[Dict], status_filter: str) -> Dict[str, int]:
    region_counts = defaultdict(int)
    for claim in claims:
        if claim.get("status") == status_filter:
            region = claim.get("region")
            region_counts[region] += 1
    return dict(region_counts)
