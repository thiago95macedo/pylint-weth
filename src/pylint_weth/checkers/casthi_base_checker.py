from __future__ import annotations

import warnings

import pylint
from pylint.checkers import BaseChecker

from .. import misc


class WETHBaseChecker(BaseChecker):
    # checks_maxmin_weth_version = {
    #   check-code: {
    #       "weth_minversion": "14.0",
    #       "weth_maxversion": "15.0",
    #   }
    checks_maxmin_weth_version: dict[str, str] = {}

    def msgid_or_symbol2symbol(self, msgid_or_symbol):
        try:
            msgid = self.linter.msgs_store.message_id_store.get_active_msgids(msgid_or_symbol)[0]
            return self.linter.msgs_store.message_id_store.get_symbol(msgid)
        except (pylint.exceptions.UnknownMessageError, IndexError):
            return None

    def is_weth_message_enabled(self, msgid):
        valid_weth_versions = self.linter.config.valid_weth_versions
        if len(valid_weth_versions) != 1:
            # It should be defined only one version
            return True
        msg_symbol = self.msgid_or_symbol2symbol(msgid)
        if msg_symbol is None:
            return True
        weth_version = valid_weth_versions[0]
        weth_version_tuple = misc.version_parse(weth_version)
        if not weth_version_tuple:
            warnings.warn(
                f"Invalid manifest versions format {weth_version}. "
                "It was not possible to supress checks based on particular weth version",
                UserWarning,
                stacklevel=2,
            )
            return True
        required_weth_versions = self.checks_maxmin_weth_version.get(msg_symbol) or {}
        weth_minversion = required_weth_versions.get("weth_minversion") or misc.DFTL_VALID_CASTHI_VERSIONS[0]
        weth_maxversion = required_weth_versions.get("weth_maxversion") or misc.DFTL_VALID_CASTHI_VERSIONS[-1]
        return (
            misc.version_parse(weth_minversion)
            <= misc.version_parse(weth_version)
            <= misc.version_parse(weth_maxversion)
        )

    def add_message(self, msgid, *args, **kwargs):
        """Emit translation-not-lazy instead of logging-not-lazy"""
        if not self.is_weth_message_enabled(msgid):
            return
        return super().add_message(msgid, *args, **kwargs)
