
"use strict";

let FileWrite = require('./FileWrite.js')
let FileRename = require('./FileRename.js')
let FileClose = require('./FileClose.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let SetMavFrame = require('./SetMavFrame.js')
let WaypointClear = require('./WaypointClear.js')
let FileList = require('./FileList.js')
let FileRead = require('./FileRead.js')
let MessageInterval = require('./MessageInterval.js')
let LogRequestData = require('./LogRequestData.js')
let StreamRate = require('./StreamRate.js')
let CommandBool = require('./CommandBool.js')
let ParamSet = require('./ParamSet.js')
let MountConfigure = require('./MountConfigure.js')
let CommandInt = require('./CommandInt.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandTOL = require('./CommandTOL.js')
let FileOpen = require('./FileOpen.js')
let ParamPull = require('./ParamPull.js')
let FileTruncate = require('./FileTruncate.js')
let CommandHome = require('./CommandHome.js')
let CommandAck = require('./CommandAck.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let LogRequestList = require('./LogRequestList.js')
let CommandLong = require('./CommandLong.js')
let FileChecksum = require('./FileChecksum.js')
let WaypointPush = require('./WaypointPush.js')
let ParamGet = require('./ParamGet.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let SetMode = require('./SetMode.js')
let ParamPush = require('./ParamPush.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let WaypointPull = require('./WaypointPull.js')
let FileRemove = require('./FileRemove.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')

module.exports = {
  FileWrite: FileWrite,
  FileRename: FileRename,
  FileClose: FileClose,
  FileRemoveDir: FileRemoveDir,
  SetMavFrame: SetMavFrame,
  WaypointClear: WaypointClear,
  FileList: FileList,
  FileRead: FileRead,
  MessageInterval: MessageInterval,
  LogRequestData: LogRequestData,
  StreamRate: StreamRate,
  CommandBool: CommandBool,
  ParamSet: ParamSet,
  MountConfigure: MountConfigure,
  CommandInt: CommandInt,
  FileMakeDir: FileMakeDir,
  CommandTOL: CommandTOL,
  FileOpen: FileOpen,
  ParamPull: ParamPull,
  FileTruncate: FileTruncate,
  CommandHome: CommandHome,
  CommandAck: CommandAck,
  LogRequestEnd: LogRequestEnd,
  LogRequestList: LogRequestList,
  CommandLong: CommandLong,
  FileChecksum: FileChecksum,
  WaypointPush: WaypointPush,
  ParamGet: ParamGet,
  CommandVtolTransition: CommandVtolTransition,
  CommandTriggerInterval: CommandTriggerInterval,
  WaypointSetCurrent: WaypointSetCurrent,
  SetMode: SetMode,
  ParamPush: ParamPush,
  VehicleInfoGet: VehicleInfoGet,
  WaypointPull: WaypointPull,
  FileRemove: FileRemove,
  CommandTriggerControl: CommandTriggerControl,
};
