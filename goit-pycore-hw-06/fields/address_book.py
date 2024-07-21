from collections import UserDict

from .record import Record


class AddressBook(UserDict):
    """Implementation of basic version of the address book."""

    def add_record(self, record: Record) -> None:
        """Add the record to the address book."""
        if record.name.value in self.data:
            raise KeyError(f"The record with name '{record.name.value}' already exists.")

        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """Find the record by name."""
        record = self.data.get(name)
        if not record:
            raise KeyError(f"The record with name '{name}' is not found.")

        return record

    def delete(self, name: str) -> None:
        """Delete the record by name."""
        if name not in self.data:
            raise KeyError(f"The record with name '{name}' is not found.")

        del self.data[name]
