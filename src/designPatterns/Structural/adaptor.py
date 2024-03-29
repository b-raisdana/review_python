class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adapted:
    """
    The Adapted contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adapted needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adapted):
    """
    The Adapter makes the Adapted's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adapted()
    print("Client: The Adapted class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adapted: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)