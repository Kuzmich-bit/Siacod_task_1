class LegacyProvider:

    def pay_legacy(self, account_id: str, amount_kopecks: int) -> int:
        if amount_kopecks <= 0:
            return 1
        if amount_kopecks > 1_000_000:
            return 2
        return 0


class AsyncProvider:

    def pay_async(self, account_id: str, amount: float, callback) -> None:
        if amount <= 0:
            callback("DECLINED")
        else:
            callback("SUCCESS")


class PollingProvider:

    def __init__(self) -> None:
        self.operations: dict[int, dict] = {}
        self.counter = 0

    def transaction(self, account_id: str, amount: float) -> int:
        self.counter += 1
        op_id = self.counter
        self.operations[op_id] = {
            "attempts": 0,
            "status": "PROCESSING"
        }
        return op_id

    def check_status(self, operation_id: int) -> str:
        if operation_id not in self.operations:
            return "UNKNOWN"

        op = self.operations[operation_id]
        op["attempts"] += 1

        if op["attempts"] >= 2:
            op["status"] = "COMPLETED"

        return op["status"]