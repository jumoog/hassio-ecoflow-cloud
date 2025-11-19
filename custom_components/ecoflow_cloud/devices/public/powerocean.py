from ...api import EcoflowApiClient
from .. import BaseDevice
from .data_bridge import to_plain

from ...sensor import (
    CelsiusSensorEntity,
    CyclesSensorEntity,
    VoltSensorEntity,
    WattsSensorEntity,
    LevelSensorEntity,
    AmpSensorEntity,
    TempSensorEntity,
    SolarPowerSensorEntity,
    SolarAmpSensorEntity,
    SystemPowerSensorEntity,
    StatusSensorEntity,
)
from ...entities import (
    BaseSensorEntity,
    BaseNumberEntity,
    BaseSwitchEntity,
    BaseSelectEntity,
)

import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)


class PowerOcean(BaseDevice):
    def flat_json(self):
        return True

    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            SolarPowerSensorEntity(client, self, "mpptPwr", "mpptPwr"),
            LevelSensorEntity(client, self, "96_8.bpSoc", "bpSoc"),
            WattsSensorEntity(client, self, "bpPwr", "bpPwr"),
            SystemPowerSensorEntity(client, self, "sysLoadPwr", "sysLoadPwr"),
            SystemPowerSensorEntity(client, self, "sysGridPwr", "sysGridPwr"),


            LevelSensorEntity(client, self, "bp1.bpSoc", "Battery 1 SoC"),
            WattsSensorEntity(client, self, "bp1.bpPwr", "Battery 1 Power"),
            AmpSensorEntity(client, self, "bp1.bpAmp", "Battery 1 Current"),
            VoltSensorEntity(client, self, "bp1.bpVol", "Battery 1 Voltage"),
            TempSensorEntity(client, self, "bp1.bpHvMosTemp", "Battery 1 HV MOS Temp"),
            TempSensorEntity(client, self, "bp1.bpLvMosTemp", "Battery 1 LV MOS Temp"),
            TempSensorEntity(client, self, "bp1.bpEnvTemp", "Battery 1 Env Temp"),
            TempSensorEntity(client, self, "bp1.bpHtsTemp", "Battery 1 Heater Temp"),
            TempSensorEntity(client, self, "bp1.bpBusPosTemp", "Battery 1 Bus + Temp"),
            TempSensorEntity(client, self, "bp1.bpBusNegTemp", "Battery 1 Bus - Temp"),
            TempSensorEntity(client, self, "bp1.bpPtcTemp", "Battery 1 PTC Temp"),
            TempSensorEntity(client, self, "bp1.bpPtcTemp2", "Battery 1 PTC Temp 2"),
            TempSensorEntity(client, self, "bp1.bpMaxCellTemp", "Battery 1 Max Cell Temp"),
            TempSensorEntity(client, self, "bp1.bpMinCellTemp", "Battery 1 Min Cell Temp"),
            CyclesSensorEntity(client, self, "bp1.bpCycles", "Battery 1 Cycles"),

            LevelSensorEntity(client, self, "bp2.bpSoc", "Battery 2 SoC"),
            WattsSensorEntity(client, self, "bp2.bpPwr", "Battery 2 Power"),
            AmpSensorEntity(client, self, "bp2.bpAmp", "Battery 2 Current"),
            TempSensorEntity(client, self, "bp2.bpHvMosTemp", "Battery 2 HV MOS Temp"),
            TempSensorEntity(client, self, "bp2.bpLvMosTemp", "Battery 2 LV MOS Temp"),
            TempSensorEntity(client, self, "bp2.bpEnvTemp", "Battery 2 Env Temp"),
            TempSensorEntity(client, self, "bp2.bpHtsTemp", "Battery 2 Heater Temp"),
            TempSensorEntity(client, self, "bp2.bpBusPosTemp", "Battery 2 Bus + Temp"),
            TempSensorEntity(client, self, "bp2.bpBusNegTemp", "Battery 2 Bus - Temp"),
            TempSensorEntity(client, self, "bp2.bpPtcTemp", "Battery 2 PTC Temp"),
            TempSensorEntity(client, self, "bp2.bpPtcTemp2", "Battery 2 PTC Temp 2"),
            TempSensorEntity(client, self, "bp2.bpMaxCellTemp", "Battery 2 Max Cell Temp"),
            TempSensorEntity(client, self, "bp2.bpMinCellTemp", "Battery 2 Min Cell Temp"),
            VoltSensorEntity(client, self, "bp2.bpVol", "Battery 2 Voltage"),
            CyclesSensorEntity(client, self, "bp2.bpCycles", "Battery 2 Cycles"),

            # String 1
            SolarPowerSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[0].pwr", "mpptPv1.pwr"
            ),
            SolarAmpSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[0].amp", "mpptPv1.amp"
            ),
            VoltSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[0].vol", "mpptPv1.vol"
            ),
            # String 2
            SolarPowerSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[1].pwr", "mpptPv2.pwr"
            ),
            SolarAmpSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[1].amp", "mpptPv2.amp"
            ),
            VoltSensorEntity(
                client, self, "96_1.mpptHeartBeat[0].mpptPv[1].vol", "mpptPv2.vol"
            ),
            VoltSensorEntity(client, self, "96_1.pcsAPhase.vol", "pcsAPhase.vol"),
            AmpSensorEntity(client, self, "96_1.pcsAPhase.amp", "pcsAPhase.amp"),
            WattsSensorEntity(
                client, self, "96_1.pcsAPhase.actPwr", "pcsAPhase.actPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsAPhase.reactPwr", "pcsAPhase.reactPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsAPhase.apparentPwr", "pcsAPhase.apparentPwr"
            ),
            VoltSensorEntity(client, self, "96_1.pcsBPhase.vol", "pcsBPhase.vol"),
            AmpSensorEntity(client, self, "96_1.pcsBPhase.amp", "pcsBPhase.amp"),
            WattsSensorEntity(
                client, self, "96_1.pcsBPhase.actPwr", "pcsBPhase.actPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsBPhase.reactPwr", "pcsBPhase.reactPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsBPhase.apparentPwr", "pcsBPhase.apparentPwr"
            ),
            VoltSensorEntity(client, self, "96_1.pcsCPhase.vol", "pcsCPhase.vol"),
            AmpSensorEntity(client, self, "96_1.pcsCPhase.amp", "pcsCPhase.amp"),
            WattsSensorEntity(
                client, self, "96_1.pcsCPhase.actPwr", "pcsCPhase.actPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsCPhase.reactPwr", "pcsCPhase.reactPwr"
            ),
            WattsSensorEntity(
                client, self, "96_1.pcsCPhase.apparentPwr", "pcsCPhase.apparentPwr"
            ),
            StatusSensorEntity(client, self),
        ]

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []

    def _prepare_data(self, raw_data) -> dict[str, "Any"]:
        res = super()._prepare_data(raw_data)
        _LOGGER.info(f"_prepare_data {raw_data}")
        res = to_plain(res)
        params = res.get("params")
        if isinstance(params, dict):
            self._inject_battery_params(params, res.get("raw_data"))
            flattened: dict[str, Any] = {}
            for key, value in list(params.items()):
                self._flatten_param_branch(key, value, flattened)
            params.update(flattened)
        return res

    def _status_sensor(self, client: EcoflowApiClient) -> StatusSensorEntity:
        return StatusSensorEntity(client, self)

    def _flatten_param_branch(
        self, prefix: str, value: Any, target: dict[str, Any]
    ) -> None:
        if isinstance(value, dict):
            for child_key, child_value in value.items():
                next_key = f"{prefix}.{child_key}"
                target[next_key] = child_value
                self._flatten_param_branch(next_key, child_value, target)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                next_key = f"{prefix}[{index}]"
                target[next_key] = item
                self._flatten_param_branch(next_key, item, target)

    def _inject_battery_params(self, params: dict[str, Any], raw_data: Any) -> None:
        if not isinstance(raw_data, dict):
            return

        # Battery heartbeat messages carry both packs; create per-pack aliases based on bpDsrc.
        heartbeat = None
        if isinstance(raw_data.get("param"), dict):
            heartbeat = raw_data.get("param", {}).get("bpHeartBeat")
        if heartbeat is None and isinstance(raw_data.get("params"), dict):
            heartbeat = raw_data.get("params", {}).get("bpHeartBeat")

        if not isinstance(heartbeat, list):
            return

        for entry in heartbeat:
            if not isinstance(entry, dict):
                continue
            dsrc = entry.get("bpDsrc")
            if dsrc not in (1, 2):
                continue
            prefix = f"bp{int(dsrc)}"
            for field, value in entry.items():
                params[f"{prefix}.{field}"] = value