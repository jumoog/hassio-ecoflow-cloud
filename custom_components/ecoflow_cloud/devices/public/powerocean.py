from ...api import EcoflowApiClient
from .. import BaseDevice
from .data_bridge import to_plain

from ...sensor import (
    CyclesSensorEntity,
    EnergySensorEntity,
    VoltSensorEntity,
    WattsSensorEntity,
    LevelSensorEntity,
    AmpSensorEntity,
    TempSensorEntity,
    MiscSensorEntity,
    MilliVoltSensorEntity,
    SolarPowerSensorEntity,
    SolarAmpSensorEntity,
    StatusSensorEntity,
)
from ...entities import (
    BaseSensorEntity,
    BaseNumberEntity,
    BaseSwitchEntity,
    BaseSelectEntity,
)

import base64
import logging
from typing import Any


class ScaledEnergySensorEntity(EnergySensorEntity):
    def __init__(
        self,
        client,
        device,
        mqtt_key,
        title,
        scale: float,
        enabled: bool = True,
        auto_enable: bool = False,
    ):
        super().__init__(client, device, mqtt_key, title, enabled, auto_enable)
        self._scale = scale

    def _update_value(self, val: Any) -> bool:
        try:
            scaled = int(val) * self._scale
        except (TypeError, ValueError):
            return False
        if scaled < 0:
            return False
        return BaseSensorEntity._update_value(self, scaled)

_LOGGER = logging.getLogger(__name__)


class PowerOcean(BaseDevice):
    def flat_json(self):
        return True

    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return [
            #SolarPowerSensorEntity(client, self, "mpptPwr", "mpptPwr"),
            LevelSensorEntity(client, self, "96_8.bpSoc", "bpSoc"),
            #WattsSensorEntity(client, self, "bpPwr", "bpPwr"),
            #SystemPowerSensorEntity(client, self, "sysLoadPwr", "sysLoadPwr"),
            #SystemPowerSensorEntity(client, self, "sysGridPwr", "sysGridPwr"),


            LevelSensorEntity(client, self, "bp1.bpSoc", "bp1Soc"),
            WattsSensorEntity(client, self, "bp1.bpPwr", "bp1Pwr"),
            AmpSensorEntity(client, self, "bp1.bpAmp", "bp1Amp"),
            VoltSensorEntity(client, self, "bp1.bpVol", "bp1Vol"),
            MilliVoltSensorEntity(client, self, "bp1.bpCellMaxVol", "bp1CellMaxVol"),
            MilliVoltSensorEntity(client, self, "bp1.bpCellMinVol", "bp1MinCellVol"),
            VoltSensorEntity(client, self, "bp1.bpBusVol", "bp1BusVol"),
            TempSensorEntity(client, self, "bp1.bpHvMosTemp", "bp1HvMosTemp"),
            TempSensorEntity(client, self, "bp1.bpLvMosTemp", "bp1LvMosTemp"),
            TempSensorEntity(client, self, "bp1.bpEnvTemp", "bp1EnvTemp"),
            TempSensorEntity(client, self, "bp1.bpHtsTemp", "bp1HtsTemp"),
            TempSensorEntity(client, self, "bp1.bpBusPosTemp", "bp1BusPosTemp"),
            TempSensorEntity(client, self, "bp1.bpBusNegTemp", "bp1BusNegTemp"),
            TempSensorEntity(client, self, "bp1.bpPtcTemp", "bp1PtcTemp"),
            TempSensorEntity(client, self, "bp1.bpPtcTemp2", "bp1PtcTemp2"),
            TempSensorEntity(client, self, "bp1.bpMaxCellTemp", "bp1MaxCellTemp"),
            TempSensorEntity(client, self, "bp1.bpMinCellTemp", "bp1MinCellTemp"),
            TempSensorEntity(client, self, "bp1.bpMaxMosTemp", "bp1MaxMosTemp"),
            TempSensorEntity(client, self, "bp1.bpMinMosTemp", "bp1MinMosTemp"),
            CyclesSensorEntity(client, self, "bp1.bpCycles", "bp1Cycles"),
            EnergySensorEntity(client, self, "bp1.bpRemainWatth", "bp1RemainWatth"),
            ScaledEnergySensorEntity(client, self, "bp1.bpAccuChgEnergy", "bp1AccuChgEnergy", 0.01),
            ScaledEnergySensorEntity(client, self, "bp1.bpAccuDsgEnergy", "bp1AccuDsgEnergy", 0.01),
            MiscSensorEntity(client, self, "bp1.bpSnDecoded", "bp1Sn"),
            MiscSensorEntity(client, self, "bp1.bmsChgDsgSta", "bp1bmsChgDsgSta"),
            MiscSensorEntity(client, self, "bp1.dabModSta", "bp1dabModSta"),
            MiscSensorEntity(client, self, "bp1.bpSysState", "bp1SysState"),
            MiscSensorEntity(client, self, "bp1.bpRunSta", "bp1RunSta"),


            LevelSensorEntity(client, self, "bp2.bpSoc", "bp2Soc"),
            WattsSensorEntity(client, self, "bp2.bpPwr", "bp2Pwr"),
            AmpSensorEntity(client, self, "bp2.bpAmp", "bp2Amp"),
            VoltSensorEntity(client, self, "bp2.bpVol", "bp2Vol"),
            MilliVoltSensorEntity(client, self, "bp2.bpCellMaxVol", "bp2CellMaxVol"),
            MilliVoltSensorEntity(client, self, "bp2.bpCellMinVol", "bp2CellMinVol"),
            VoltSensorEntity(client, self, "bp2.bpBusVol", "bp2BusVol"),
            TempSensorEntity(client, self, "bp2.bpHvMosTemp", "bp2HvMosTemp"),
            TempSensorEntity(client, self, "bp2.bpLvMosTemp", "bp2LvMosTemp"),
            TempSensorEntity(client, self, "bp2.bpEnvTemp", "bp2EnvTemp"),
            TempSensorEntity(client, self, "bp2.bpHtsTemp", "bp2HtsTemp"),
            TempSensorEntity(client, self, "bp2.bpBusPosTemp", "bp2BusPosTemp"),
            TempSensorEntity(client, self, "bp2.bpBusNegTemp", "bp2BusNegTemp"),
            TempSensorEntity(client, self, "bp2.bpPtcTemp", "bp2PtcTemp"),
            TempSensorEntity(client, self, "bp2.bpPtcTemp2", "bp2PtcTemp2"),
            TempSensorEntity(client, self, "bp2.bpMaxCellTemp", "bp2MaxCellTemp"),
            TempSensorEntity(client, self, "bp2.bpMinCellTemp", "bp2MinCellTemp"),
            TempSensorEntity(client, self, "bp2.bpMaxMosTemp", "bp2MaxMosTemp"),
            TempSensorEntity(client, self, "bp2.bpMinMosTemp", "bp2MinMosTemp"),
            CyclesSensorEntity(client, self, "bp2.bpCycles", "bp2Cycles"),
            EnergySensorEntity(client, self, "bp2.bpRemainWatth", "bp2RemainWatth"),
            ScaledEnergySensorEntity(client, self, "bp2.bpAccuChgEnergy", "bp2AccuChgEnergy", 0.01),
            ScaledEnergySensorEntity(client, self, "bp2.bpAccuDsgEnergy", "bp2AccuDsgEnergy", 0.01),
            MiscSensorEntity(client, self, "bp2.bpSnDecoded", "bp2Sn"),
            MiscSensorEntity(client, self, "bp2.bmsChgDsgSta", "bp2bmsChgDsgSta"),
            MiscSensorEntity(client, self, "bp2.dabModSta", "bp2dabModSta"),
            MiscSensorEntity(client, self, "bp2.bpSysState", "bp2SysState"),
            MiscSensorEntity(client, self, "bp2.bpRunSta", "bp2RunSta"),

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

            bp_sn = entry.get("bpSn")
            if isinstance(bp_sn, str):
                try:
                    decoded_sn = base64.b64decode(bp_sn).decode("utf-8")
                except Exception:  # noqa: BLE001
                    decoded_sn = None
                if decoded_sn:
                    params[f"{prefix}.bpSnDecoded"] = decoded_sn