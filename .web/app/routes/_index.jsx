

import { Fragment, useCallback, useContext, useEffect } from "react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Container as RadixThemesContainer, Flex as RadixThemesFlex, Heading as RadixThemesHeading, Link as RadixThemesLink, Separator as RadixThemesSeparator, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import DebounceInput from "react-debounce-input"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event, isNotNullOrUndefined, isTrue } from "$/utils/state"
import { Link as ReactRouterLink } from "react-router"
import { jsx } from "@emotion/react"



function Flex_140171163857450892242511283845636323386 () {
  
  const reflex___state____state__benchmark_demo___benchmark_demo____app_state = useContext(StateContexts.reflex___state____state__benchmark_demo___benchmark_demo____app_state)





  
  return (
    jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"5"},
reflex___state____state__benchmark_demo___benchmark_demo____app_state.turns_rx_state_.map((turn_rx_state_,index_e3cf23fa7bba6c91)=>(jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",key:index_e3cf23fa7bba6c91,gap:"3"},
jsx(
RadixThemesBox,
{css:({ ["border"] : "1px solid #2a2f3a", ["background"] : "#14161a", ["borderRadius"] : "12px", ["padding"] : "10px", ["width"] : "100%" })},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" }),weight:"bold"},
"You"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
turn_rx_state_["user"]
,),),jsx(
Fragment,
{},
(!((turn_rx_state_["logs_text"] === "")) ? (jsx(
Fragment,
{},
jsx(
RadixThemesBox,
{css:({ ["border"] : "1px dashed #2a2f3a", ["background"] : "#14161a", ["borderRadius"] : "12px", ["padding"] : "10px", ["width"] : "100%" })},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" }),weight:"bold"},
"Logs"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
turn_rx_state_["logs_text"]
,),),)) : (jsx(Fragment,{},)
)),),jsx(
RadixThemesBox,
{css:({ ["width"] : "100%" })},
turn_rx_state_["models"].map((m_rx_state_,index_ed9b9ca7243242f4)=>(jsx(
RadixThemesBox,
{css:({ ["border"] : "1px solid #2a2f3a", ["borderRadius"] : "12px", ["padding"] : "14px", ["width"] : "100%", ["background"] : "#14161a" }),key:index_ed9b9ca7243242f4},
jsx(
RadixThemesBox,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(
RadixThemesText,
{as:"p"},
"\ud83e\udde0"
,),jsx(
RadixThemesHeading,
{css:({ ["color"] : "#e5e7eb" }),size:"6"},
m_rx_state_["name"]
,),),jsx(
RadixThemesLink,
{css:({ ["color"] : "#60a5fa", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),href:"#",underline:"always"},
"Open model card \u2197"
,m_rx_state_["source_url"]
,),jsx(RadixThemesSeparator,{css:({ ["marginTop"] : "8px", ["marginBottom"] : "8px", ["borderColor"] : "#2a2f3a" }),size:"4"},)
,jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83c\udfaf Task: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["task"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83e\uddee Params: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["params"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\u26a1 Latency: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["latency"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83d\uddc4\ufe0f  Memory: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["memory_footprint"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83d\udcdc License: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["license"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83d\udd13 Openness: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["openness"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83e\uddea Benchmarks: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["benchmarks_text"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\u2705 Good for: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["recommended_text"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83d\udc4d Strengths: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["strengths_text"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\u26a0\ufe0f Limitations: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["limitations_text"]
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"\ud83d\udcdd Summary: "
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
m_rx_state_["description"]
,),),),),))),),jsx(
Fragment,
{},
(!((turn_rx_state_["recommendation"] === "")) ? (jsx(
Fragment,
{},
jsx(
RadixThemesBox,
{css:({ ["border"] : "1px solid #2a2f3a", ["background"] : "#14161a", ["borderRadius"] : "12px", ["padding"] : "10px", ["width"] : "100%" })},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" }),weight:"bold"},
"Recommendation"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
turn_rx_state_["recommendation"]
,),),)) : (jsx(Fragment,{},)
)),),))),)
  )
}

function Button_262699281034490842119079443622372898260 () {
  
  const reflex___state____state__benchmark_demo___benchmark_demo____app_state = useContext(StateContexts.reflex___state____state__benchmark_demo___benchmark_demo____app_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_60c99187c0a8119eebb3f2d679d78a27 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.benchmark_demo___benchmark_demo____app_state.run_benchmark", ({  }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{css:({ ["background"] : "#14161a", ["border"] : "1px solid #2a2f3a", ["borderRadius"] : "10px" }),disabled:reflex___state____state__benchmark_demo___benchmark_demo____app_state.running_rx_state_,onClick:on_click_60c99187c0a8119eebb3f2d679d78a27},
jsx(Fragment_44947626339899136820476717949939523858,{},)
,)
  )
}

function Fragment_44947626339899136820476717949939523858 () {
  
  const reflex___state____state__benchmark_demo___benchmark_demo____app_state = useContext(StateContexts.reflex___state____state__benchmark_demo___benchmark_demo____app_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__benchmark_demo___benchmark_demo____app_state.running_rx_state_ ? (jsx(
Fragment,
{},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
"Running\u2026"
,),)) : (jsx(
Fragment,
{},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#e5e7eb" })},
"Run"
,),))),)
  )
}

function Debounceinput_169659274119948761052214120614947837796 () {
  
  const reflex___state____state__benchmark_demo___benchmark_demo____app_state = useContext(StateContexts.reflex___state____state__benchmark_demo___benchmark_demo____app_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_10c6e2d4cf07860e192b36cacf89cf47 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.benchmark_demo___benchmark_demo____app_state.set_query", ({ ["q"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(DebounceInput,{css:({ ["width"] : "100%", ["color"] : "#e5e7eb", ["background"] : "#14161a", ["border"] : "1px solid #2a2f3a" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_10c6e2d4cf07860e192b36cacf89cf47,placeholder:"Ask anything (e.g., 'fast NLP models for QA')",value:(isNotNullOrUndefined(reflex___state____state__benchmark_demo___benchmark_demo____app_state.query_rx_state_) ? reflex___state____state__benchmark_demo___benchmark_demo____app_state.query_rx_state_ : "")},)

  )
}

export default function Component() {
    




  return (
    jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["minH"] : "100vh", ["background"] : "#0b0b0b" })},
jsx(
RadixThemesContainer,
{css:({ ["padding"] : "16px", ["maxWidth"] : "900px" }),size:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingTop"] : "2rem", ["paddingBottom"] : "2rem" }),direction:"column",gap:"5"},
jsx(
RadixThemesHeading,
{css:({ ["color"] : "#e5e7eb" }),size:"6"},
"AI Benchmark Evaluation Agent (Demo)"
,),jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "#9ca3af" })},
"Type a question, click Run. Each turn is saved below so you can continue the conversation."
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},
jsx(Debounceinput_169659274119948761052214120614947837796,{},)
,jsx(Button_262699281034490842119079443622372898260,{},)
,),jsx(Flex_140171163857450892242511283845636323386,{},)
,),),),jsx(
"title",
{},
"BenchmarkDemo | Index"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,)
  )
}
