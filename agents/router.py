class ResurrectionRouter:
    def __init__(self):
        self.avg_gas_cost_usd = {
            "Ethereum": 3.50,
            "Arbitrum": 0.15,
            "Optimism": 0.10,
            "X_Layer": 0.05
        }

    def filter_profitable_assets(self, assets: list):
        """
        Filters out scam tokens and dust where recovery gas > asset value.
        """
        profitable_assets = []
        total_gas = 0.0

        for asset in assets:
            if asset.get("is_scam"):
                continue
                
            chain = asset["chain"]
            est_gas = self.avg_gas_cost_usd.get(chain, 0.50)
            
            # 只有当资产价值大于 Gas 费时，才值得唤醒
            if asset["value_usd"] > est_gas:
                profitable_assets.append(asset)
                total_gas += est_gas

        return profitable_assets, total_gas
