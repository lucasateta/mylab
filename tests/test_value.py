import pytest

from XYZThings.models.value import Value

@pytest.mark.asyncio
async def test_set_value_with_action():
    # Arrange

    v = Value(1)

    updated_values = []
    @v.on('update')
    def on_value_updated(updated_value):
        updated_values.append(updated_value)

    # Action
    await v.set(3)
    await v.set(4)

    # Assert
    assert await v.get() == 4
    assert updated_values == [3, 4]

@pytest.mark.asyncio
async def test_set_value_with_action_not():
    # Arrange
    v = Value(1)
    synced_values = []
    @v.on('sync')
    def on_value_synced(synced_value):
        synced_values.append(synced_value)

    await v.set(3, with_action=False)
    await v.set(4, with_action=False)

    assert synced_values == [3, 4]

    assert await v.get() == 4

@pytest.mark.asyncio
async def test_set_value_with_forwarder():
    # Arrange
    forwarded_values = []
    def value_forwarder(new_value):
        forwarded_values.append(new_value)

    v = Value(1, value_forwarder=value_forwarder)

    await v.set(3)
    await v.set(4)

    assert forwarded_values == [1, 3, 4]

    assert await v.get() == 4
